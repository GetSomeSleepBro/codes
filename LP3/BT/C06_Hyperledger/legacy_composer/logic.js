/**
 * BT Assignment 6 - Transaction processor function (lib/logic.js)
 */
'use strict';

/**
 * Trade a vehicle to a new owner
 * @param {org.example.trading.Trade} trade - the trade transaction
 * @transaction
 */
async function tradeVehicle(trade) {
    const vehicle = trade.vehicle;
    const buyer = trade.newOwner;
    const seller = vehicle.owner;

    if (buyer.balance < vehicle.price) {
        throw new Error('Buyer does not have enough balance');
    }

    // Move money and ownership
    buyer.balance -= vehicle.price;
    seller.balance += vehicle.price;
    vehicle.owner = buyer;

    const assetRegistry = await getAssetRegistry('org.example.trading.Vehicle');
    await assetRegistry.update(vehicle);

    const participantRegistry = await getParticipantRegistry('org.example.trading.Trader');
    await participantRegistry.updateAll([buyer, seller]);

    // Emit event
    const event = getFactory().newEvent('org.example.trading', 'TradeNotification');
    event.vehicle = vehicle;
    event.oldOwner = seller.traderId;
    event.newOwner = buyer.traderId;
    emit(event);
}
