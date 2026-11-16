'use strict';
const { Contract } = require('fabric-contract-api');
class BusinessNetwork extends Contract {
  async CreateTrader(ctx, id, firstName, lastName, balanceText) {
    if (!id || !firstName || !lastName) throw new Error('Trader ID and name required');
    if (await ctx.stub.getState('trader:' + id).then(b => b.length > 0)) throw new Error('Trader exists');
    const balance = Number(balanceText);
    if (!Number.isSafeInteger(balance) || balance < 0) throw new Error('Balance must be nonnegative integer cents');
    const trader = { docType: 'trader', id, firstName, lastName, balance };
    await ctx.stub.putState('trader:' + id, Buffer.from(JSON.stringify(trader)));
    return JSON.stringify(trader);
  }
  async CreateVehicle(ctx, vin, make, model, priceText, ownerId) {
    if (!vin || !make || !model) throw new Error('VIN, make and model required');
    if ((await ctx.stub.getState('vehicle:' + vin)).length) throw new Error('Vehicle exists');
    if (!(await ctx.stub.getState('trader:' + ownerId)).length) throw new Error('Owner not found');
    const price = Number(priceText);
    if (!Number.isSafeInteger(price) || price < 0) throw new Error('Price must be nonnegative integer cents');
    const vehicle = { docType: 'vehicle', vin, make, model, price, ownerId };
    await ctx.stub.putState('vehicle:' + vin, Buffer.from(JSON.stringify(vehicle)));
    return JSON.stringify(vehicle);
  }
  async ReadTrader(ctx, id) {
    const bytes = await ctx.stub.getState('trader:' + id);
    if (!bytes.length) throw new Error('Trader not found');
    return bytes.toString();
  }
  async ReadVehicle(ctx, vin) {
    const bytes = await ctx.stub.getState('vehicle:' + vin);
    if (!bytes.length) throw new Error('Vehicle not found');
    return bytes.toString();
  }
  async TradeVehicle(ctx, vin, buyerId) {
    const vehicle = JSON.parse(await this.ReadVehicle(ctx, vin));
    const buyer = JSON.parse(await this.ReadTrader(ctx, buyerId));
    const sellerId = vehicle.ownerId;
    if (sellerId === buyerId) throw new Error('Buyer is already owner');
    const seller = JSON.parse(await this.ReadTrader(ctx, sellerId));
    if (buyer.balance < vehicle.price) throw new Error('Insufficient balance');
    buyer.balance -= vehicle.price;
    seller.balance += vehicle.price;
    if (!Number.isSafeInteger(seller.balance)) throw new Error('Balance overflow');
    vehicle.ownerId = buyerId;
    await ctx.stub.putState('trader:' + buyerId, Buffer.from(JSON.stringify(buyer)));
    await ctx.stub.putState('trader:' + sellerId, Buffer.from(JSON.stringify(seller)));
    await ctx.stub.putState('vehicle:' + vin, Buffer.from(JSON.stringify(vehicle)));
    ctx.stub.setEvent('VehicleTraded', Buffer.from(JSON.stringify({ vin, from: sellerId, to: buyerId })));
    return JSON.stringify(vehicle);
  }
}
module.exports = BusinessNetwork;
