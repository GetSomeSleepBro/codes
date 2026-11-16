# SPPU BE Computer Engineering — LP-III
## ML & Blockchain Technology: Theory and Viva Q&A

**Pattern:** 2019 | **Semester:** VII | **Subjects:** Machine Learning (Group B) and Blockchain Technology (Group C)

> **Scope:** Covers only the six questions shown in the supplied question sheet: **B(2), B(3), B(4), the Titanic mini-project, C(1), and C(2)**. This is an oral-exam theory guide—not a source-code file.
>
> **How to revise:** Read the **Aim → Theory → Working → Key Points** for each practical, then practise answering the viva questions in 1–3 sentences.

---

# PART I — MACHINE LEARNING (ML)

## B(2) — Email Spam Detection Using KNN and SVM

### Question / Aim
Classify emails into **Normal (Not Spam)** and **Abnormal (Spam)** using **K-Nearest Neighbors (KNN)** and **Support Vector Machine (SVM)**, and compare their performance.

### Theory
- **Binary classification** is supervised learning that predicts one of two classes. Here, typically **0 = Not Spam** and **1 = Spam**.
- A labelled email dataset is used to train and evaluate the classifiers. Email text can be represented numerically using word frequencies or other extracted features.
- **KNN** predicts a new email's class by examining the **K nearest labelled examples** in feature space and taking a majority vote.
- **SVM** finds a decision boundary (hyperplane) that separates the classes, aiming for a large margin. Kernel-based SVM can model more complex boundaries.
- **Preprocessing:** Handle missing data, separate features and labels, split training/testing data, and scale features when needed—especially for distance-based KNN.
- **Performance metrics:** Accuracy, precision, recall, F1-score and confusion matrix. For spam, precision means fewer legitimate emails are incorrectly flagged; recall means fewer spam emails are missed.

### Working / Algorithm
1. Load labelled email data and identify the target class.
2. Prepare numerical email features; split data into training and testing sets.
3. Train KNN and SVM on the training portion.
4. Predict labels for the same held-out test portion.
5. Compare their accuracy, precision, recall, F1-score and confusion matrices.

### Complexity / Key Points
- **KNN:** Training is mainly storage; basic prediction compares a new sample with many training samples, taking roughly **O(N × D)** per sample for N training emails and D features.
- **SVM:** Training cost depends on the solver, dataset size, number of features and kernel; there is no single fixed time complexity for all SVMs.
- **Important:** A higher accuracy alone does not prove that the spam classifier is better if the classes are imbalanced.

### Viva Questions & Answers

**Q1. What is spam detection?**  
**Ans:** Automatically deciding whether an email is unwanted/spam or legitimate/not spam.

**Q2. What is binary classification?**  
**Ans:** A supervised learning task with exactly two possible output classes.

**Q3. What is supervised learning?**  
**Ans:** Learning a relationship from input features and their known correct labels.

**Q4. What is KNN?**  
**Ans:** A distance-based classifier that predicts a class using the majority class among its K nearest training samples.

**Q5. What does K mean in KNN?**  
**Ans:** The number of nearest neighbours considered for prediction.

**Q6. Why is feature scaling important for KNN?**  
**Ans:** KNN uses distances, so large-valued features can dominate if features are on different scales.

**Q7. What is SVM?**  
**Ans:** A classifier that tries to separate classes with a decision boundary having a large margin.

**Q8. What is a hyperplane?**  
**Ans:** A decision boundary that separates classes in the feature space.

**Q9. What are support vectors?**  
**Ans:** Training examples near the decision boundary that influence the SVM's optimal margin.

**Q10. What is a kernel in SVM?**  
**Ans:** A method for creating nonlinear decision boundaries by implicitly comparing data in a transformed feature space.

**Q11. Which is better, KNN or SVM?**  
**Ans:** Neither is always better. Compare both on the same held-out dataset using meaningful evaluation metrics and prediction cost.

**Q12. What is a confusion matrix?**  
**Ans:** A table showing correct and incorrect predictions: true positives, true negatives, false positives and false negatives.

**Q13. What do precision and recall mean in spam detection?**  
**Ans:** Precision measures how many emails marked spam really are spam; recall measures how much of the actual spam was detected.

**Q14. What is F1-score?**  
**Ans:** The harmonic mean of precision and recall; useful when both false positives and false negatives matter.

**Q15. What is overfitting?**  
**Ans:** When a model learns training-specific patterns but performs poorly on unseen emails.

**Q16. Why use a train-test split?**  
**Ans:** To evaluate how well the model generalizes to emails it did not learn from.

**Conclusion:** KNN and SVM can classify email as spam or not spam. Their quality should be judged from unseen-data performance, not only training accuracy.

---

## B(3) — Bank Customer Churn Prediction Using a Neural Network

### Question / Aim
Build a **neural-network-based binary classifier** to predict whether a bank customer will **leave or stay** in the next six months.

### Theory
- **Customer churn** means a customer stops using the bank's service or leaves the bank.
- **Artificial Neural Network (ANN):** A learning model consisting of connected units (*neurons*) organized into input, hidden and output layers.
- **Input features** may include age, credit score, account balance, geography, gender, tenure, product count, and activity indicators.
- **Output:** A single predicted probability of churn, often converted into a class: **0 = Stays**, **1 = Leaves**.
- **Activation functions** introduce nonlinearity. **ReLU** is common in hidden layers; **sigmoid** is common for a binary output probability.
- **Training:** Forward pass → calculate loss → backpropagation → optimizer updates weights. Repeat over epochs.
- **Preprocessing:** Encode categorical columns, scale numerical values when appropriate, handle missing values, and separate training and testing data.
- **Evaluation:** Confusion matrix, accuracy, precision, recall and F1-score. Recall may be particularly important when missing likely-to-leave customers is costly.

**Dataset qualification:** The commonly used `Churn_Modelling.csv` dataset contains a historical `Exited` label. Unless the data explicitly records a six-month observation window, this dataset demonstrates **churn classification**, but does **not independently verify the six-month prediction horizon** in the question.

### Working / Algorithm
1. Load bank records; identify inputs and the churn target.
2. Encode categorical columns, scale features and create train/test sets.
3. Define ANN input, hidden and binary-output layers.
4. Train the network by minimizing prediction loss.
5. Predict churn on test data and calculate evaluation metrics.

### Complexity / Key Points
- The cost of training depends on **number of samples, features, neurons, layers and epochs**.
- More layers/neurons do not always improve test performance; they can increase overfitting.
- Predictions are statistical estimates, **not guaranteed future behaviour**.

### Viva Questions & Answers

**Q1. What is customer churn?**  
**Ans:** The loss of customers when they stop using a bank's products or services.

**Q2. Is this regression or classification?**  
**Ans:** Binary classification, because the target has two classes: leave or stay.

**Q3. What is an ANN?**  
**Ans:** A model of connected computational neurons that learns patterns by adjusting weights during training.

**Q4. What are the layers in an ANN?**  
**Ans:** Input layer receives features; hidden layers learn patterns; output layer produces the prediction.

**Q5. What is a neuron?**  
**Ans:** A unit that combines weighted inputs and a bias, then applies an activation function.

**Q6. What is an activation function?**  
**Ans:** A function that enables the network to learn nonlinear relationships.

**Q7. Why use ReLU?**  
**Ans:** It is simple and helps hidden layers learn nonlinear relationships efficiently.

**Q8. Why use sigmoid in the output layer?**  
**Ans:** It maps the output to a value between 0 and 1 for binary classification.

**Q9. What is an epoch?**  
**Ans:** One full pass through the training dataset.

**Q10. What is a loss function?**  
**Ans:** A measure of prediction error that the model tries to minimize during training.

**Q11. What is backpropagation?**  
**Ans:** Calculating how each network weight contributes to the loss, so an optimizer can update the weights.

**Q12. What is an optimizer?**  
**Ans:** The training method that adjusts weights to reduce loss, such as gradient descent or Adam.

**Q13. Why encode geography or gender?**  
**Ans:** Most neural networks require numerical input, while such fields may be categorical.

**Q14. Why scale numerical features?**  
**Ans:** To keep feature magnitudes comparable and usually make optimization more stable.

**Q15. What is overfitting and how can it be reduced?**  
**Ans:** When training performance is high but test performance is poor. Use validation, early stopping, regularization or a simpler network.

**Q16. Can the model guarantee churn within six months?**  
**Ans:** No. It estimates risk from historical labels; a true six-month forecast needs data with that specific time horizon.

**Conclusion:** An ANN learns relationships in customer data to estimate churn risk, helping banks identify customers who may need retention attention.

---

## B(4) — Diabetes Prediction Using K-Nearest Neighbors

### Question / Aim
Apply **KNN** to `diabetes.csv` and calculate the **confusion matrix, accuracy, error rate, precision and recall**.

### Theory
- The diabetes dataset is a **binary classification** problem: typically **0 = No diabetes** and **1 = Diabetes** according to its target label (`Outcome`).
- **KNN** is a supervised, instance-based algorithm: it classifies a new record based on the majority class of its K nearest examples.
- A commonly used distance measure is **Euclidean distance**; numerical attributes should usually be scaled so one measurement does not dominate the distance.
- Split the dataset into training and test records; avoid fitting preprocessing steps on the test data.
- **Confusion-matrix terms:**
  - **TP:** Diabetes correctly predicted as diabetes.
  - **TN:** No diabetes correctly predicted as no diabetes.
  - **FP:** No diabetes incorrectly predicted as diabetes.
  - **FN:** Diabetes incorrectly predicted as no diabetes.

### Essential Metrics

| Metric | Formula | Meaning |
|---|---|---|
| Accuracy | `(TP + TN) / (TP + TN + FP + FN)` | Fraction of all correct predictions |
| Error rate | `(FP + FN) / Total` or `1 − Accuracy` | Fraction of incorrect predictions |
| Precision | `TP / (TP + FP)` | How many positive predictions were correct |
| Recall / Sensitivity | `TP / (TP + FN)` | How many actual positive cases were detected |
| F1-score | `2 × Precision × Recall / (Precision + Recall)` | Balance of precision and recall |
| Specificity | `TN / (TN + FP)` | How many actual negative cases were detected |

> A metric with a zero denominator requires a defined zero-division handling rule. In machine-learning libraries, that can be configured explicitly.

### Working / Algorithm
1. Load `diabetes.csv` and separate attributes from the `Outcome` target.
2. Split into training and testing data.
3. Fit scaling on training data and apply it to both splits.
4. Train KNN with a selected K value and predict test labels.
5. Display the confusion matrix and compute the requested metrics.

### Complexity / Key Points
- **Basic KNN prediction:** Approximately **O(N × D)** per query for N training records and D features.
- **Storage:** Approximately **O(N × D)** for the stored training features.
- A **small K** can be sensitive to noise; a **large K** can smooth away important class boundaries.
- For healthcare-related classification, recall matters when missing a positive case has significant consequences. The classroom model is not a clinical diagnostic system.

### Viva Questions & Answers

**Q1. What is KNN?**  
**Ans:** A classifier that chooses the majority label among the K closest training samples.

**Q2. Is KNN supervised or unsupervised?**  
**Ans:** Supervised, because it uses labelled training examples.

**Q3. What is the target in this dataset?**  
**Ans:** `Outcome`, representing the two diabetes classification labels.

**Q4. What does K represent?**  
**Ans:** The number of nearest neighbours used for prediction.

**Q5. What is Euclidean distance?**  
**Ans:** Straight-line distance between two points in feature space.

**Q6. Why is scaling necessary?**  
**Ans:** Features with large values could otherwise dominate the distance calculation.

**Q7. What is a confusion matrix?**  
**Ans:** A summary of TP, TN, FP and FN predictions.

**Q8. What is accuracy?**  
**Ans:** Correct predictions divided by all predictions.

**Q9. What is error rate?**  
**Ans:** Incorrect predictions divided by all predictions; equals 1 minus accuracy.

**Q10. What is precision?**  
**Ans:** The proportion of predicted positive cases that are truly positive.

**Q11. What is recall?**  
**Ans:** The proportion of actual positive cases that the model detects.

**Q12. What is a false positive?**  
**Ans:** The model predicts diabetes for a record labelled as not diabetic.

**Q13. What is a false negative?**  
**Ans:** The model predicts no diabetes for a record labelled as diabetic.

**Q14. Which metric is important when missing positive cases is risky?**  
**Ans:** Recall, because it measures how many actual positives are detected; precision must still be considered.

**Q15. How do we choose K?**  
**Ans:** Compare candidate K values using validation data and appropriate performance metrics.

**Q16. Does high accuracy always mean a good classifier?**  
**Ans:** No. Accuracy can be misleading with imbalanced classes; inspect precision, recall and the confusion matrix.

**Conclusion:** KNN classifies diabetes records by similarity, and its performance is measured using the confusion matrix, accuracy, error rate, precision and recall.

---

## ML Mini-Project — Titanic Survival Prediction

### Question / Aim
Build a machine-learning model to predict **which types of passengers survived the Titanic shipwreck**, using passenger details such as **name, age, gender and socio-economic class**.

### Theory
- This is a **supervised binary classification** task: **1 = Survived**, **0 = Did not survive**.
- The Kaggle Titanic `train.csv` dataset contains **891 labelled passengers** and **12 columns**, including the survival target.
- Common inputs include **Pclass** (ticket class, a proxy for socio-economic status), **Sex, Age, SibSp, Parch, Fare** and **Embarked**. Name may also be used to derive titles or other features.
- Real passenger records can contain **missing values** such as unknown age or embarkation location, so preprocessing is necessary.
- A suitable classifier is **Random Forest**, which combines predictions from several decision trees. Other valid choices include logistic regression and decision trees.
- The model learns **historical associations**, not guaranteed rules or causal explanations about survival.

### Working / Algorithm
1. Load the labelled Titanic training dataset.
2. Choose useful passenger characteristics and the `Survived` target.
3. Handle missing data; encode categorical features; split training/testing data.
4. Train a classifier such as Random Forest.
5. Predict survival on held-out passengers and evaluate accuracy, precision, recall, F1-score and the confusion matrix.
6. Use the trained model to estimate survival for a new, consistently formatted passenger record.

### Complexity / Key Points
- Random Forest training and prediction costs depend on **number of trees, tree depth, training samples and features**.
- More trees usually require more computation and memory.
- **Data leakage:** Never use actual survival outcomes or information unavailable at prediction time as features.
- **Ethical note:** Patterns related to gender and class describe this historical dataset; the model should not be treated as a statement about individual worth or destiny.

### Viva Questions & Answers

**Q1. What is the goal of the Titanic mini-project?**  
**Ans:** Predict passenger survival from recorded characteristics using a supervised ML classifier.

**Q2. Is this classification or regression?**  
**Ans:** Binary classification, because the outcome is survived or not survived.

**Q3. What is the target column?**  
**Ans:** `Survived`, where 1 indicates survival and 0 indicates non-survival.

**Q4. How many training records are in Kaggle's Titanic dataset?**  
**Ans:** 891 passenger records in `train.csv`.

**Q5. What does Pclass represent?**  
**Ans:** Passenger ticket class—first, second or third—and a rough indicator of socio-economic position.

**Q6. What is feature selection?**  
**Ans:** Choosing relevant input columns that help predict the target.

**Q7. Why handle missing ages?**  
**Ans:** Many classifiers cannot directly use missing numeric values, so they must be imputed or handled by a compatible model.

**Q8. Why encode Sex and Embarked?**  
**Ans:** They are categorical values that must be represented numerically for many ML algorithms.

**Q9. What is Random Forest?**  
**Ans:** An ensemble of decision trees whose combined votes produce a classification.

**Q10. What is a decision tree?**  
**Ans:** A model that repeatedly splits data using feature-based questions to reach a prediction.

**Q11. Why use multiple trees instead of one?**  
**Ans:** Combining trees often improves generalization and reduces instability compared with a single tree.

**Q12. What is training versus testing?**  
**Ans:** Training is learning patterns; testing measures performance on records not used for learning.

**Q13. What is overfitting?**  
**Ans:** Memorizing training-specific patterns instead of learning useful general relationships.

**Q14. Which metrics evaluate the classifier?**  
**Ans:** Confusion matrix, accuracy, precision, recall and F1-score.

**Q15. What is data leakage?**  
**Ans:** When test information or information unavailable at prediction time influences training and produces misleadingly high scores.

**Q16. Can the model perfectly predict who would have survived?**  
**Ans:** No. It estimates outcomes from incomplete historical records and observed patterns.

**Conclusion:** The Titanic mini-project applies classification and preprocessing to historical passenger data to estimate the likelihood of survival.

---

# PART II — BLOCKCHAIN TECHNOLOGY (BT)

## C(1) — Student Data Smart Contract: Structures, Arrays, Fallback, Gas

### Question / Aim
Create student records in **Solidity** using **structures, arrays and a fallback function**. Deploy the smart contract in an Ethereum-compatible environment and observe **transaction fees and gas values**.

### Theory
- **Blockchain:** A distributed ledger where transactions are recorded in blocks and validated according to network rules.
- **Ethereum:** A blockchain platform that supports programmable **smart contracts**.
- **Solidity:** A high-level programming language commonly used to write Ethereum smart contracts.
- **Smart contract:** Code deployed at a blockchain address that executes on transactions or calls.
- **Structure (`struct`):** A user-defined data type combining related fields; here, a student record may include ID, name, age and enrolment status.
- **Array:** A collection of elements; it can store multiple student records. A dynamic array can grow as records are added.
- **Fallback function:** Runs when a call does not match another function, or for certain ETH transfers when no suitable receive function exists. A fallback declared payable can accept ETH.
- **Receive function:** A dedicated payable function for plain ETH transfers with empty calldata. If both receive and fallback exist, plain transfers generally trigger **receive**, not fallback.
- **Gas:** A unit measuring EVM execution/resource usage. **Transaction fee ≈ gas used × effective gas price**. Gas price is normally expressed in **gwei**; one ETH equals **10⁹ gwei**.
- **Remix VM:** A local simulated blockchain useful for demonstrations, with funded test accounts; its ETH and transaction costs are **simulated**. A public Ethereum testnet requires its own test ETH for deployment transactions.

### Working / Practical Steps (Conceptual)
1. Write and compile the Solidity student-record contract in Remix.
2. Deploy it using **Remix VM** for a local demonstration, or an approved testnet if required.
3. Add student details and verify that they can be retrieved.
4. Check that multiple student records are stored in the array.
5. Trigger the appropriate fallback behaviour using a call with an unrecognized function selector, and distinguish it from a plain ETH transfer.
6. Inspect the deployment and method transactions; record **gas used**, **gas price** and **transaction fee** where shown.

### Complexity / Key Points
- A blockchain **state-changing transaction costs gas**; a local read-only call typically does not require the caller to send a payable transaction.
- **Gas used is not the same as gas price**: one measures work, the other determines the cost per gas unit.
- On-chain data is generally public; do **not** place sensitive personal student data on a public blockchain for real use.

### Viva Questions & Answers

**Q1. What is blockchain?**  
**Ans:** A distributed ledger that records validated transactions in linked blocks.

**Q2. What is Ethereum?**  
**Ans:** A programmable blockchain that supports smart contracts and transactions.

**Q3. What is Solidity?**  
**Ans:** A programming language used to develop EVM-compatible smart contracts.

**Q4. What is a smart contract?**  
**Ans:** A program deployed on a blockchain that follows its coded rules when invoked.

**Q5. What is a structure?**  
**Ans:** A custom type that groups related fields into one record, such as a student profile.

**Q6. Why use an array?**  
**Ans:** To hold multiple student records in an ordered collection.

**Q7. What is a dynamic array?**  
**Ans:** An array whose length can increase as new elements are added.

**Q8. What is a fallback function?**  
**Ans:** A special function called when no matching function is found, or in particular ETH-receiving cases.

**Q9. What is the difference between receive and fallback?**  
**Ans:** `receive` handles plain ETH transfers with empty calldata; `fallback` handles unmatched calls and may handle ETH when no receive function exists.

**Q10. What does payable mean?**  
**Ans:** It allows a function to accept an ETH value with the transaction.

**Q11. What is gas?**  
**Ans:** The measure of computational/resource effort charged for Ethereum execution.

**Q12. What is the transaction fee?**  
**Ans:** The cost paid for executing a transaction, approximately gas used multiplied by effective gas price.

**Q13. What is gwei?**  
**Ans:** A denomination of ETH used for quoting gas prices; 1 gwei is 10⁻⁹ ETH.

**Q14. Why does adding a student cost gas?**  
**Ans:** It changes blockchain state by storing data, so validators must execute and record the transaction.

**Q15. What is the purpose of Remix IDE?**  
**Ans:** To write, compile, deploy, test and inspect Solidity smart contracts in a browser.

**Q16. Can Remix VM be used without MetaMask or faucet ETH?**  
**Ans:** Yes. Remix VM provides simulated accounts and ETH for local practice; a real public testnet needs a wallet and test ETH for transactions.

**Q17. Why should we record gas used and gas price separately?**  
**Ans:** Gas used measures work, while gas price determines the per-unit charge; both affect the transaction fee.

**Q18. Does a successful compilation prove the contract is secure?**  
**Ans:** No. Compilation checks syntax and some correctness conditions; testing and security review are still required.

**Conclusion:** Student records demonstrate Solidity structures and arrays, while fallback/receive functions and transaction receipts illustrate contract interaction and gas costs.

---

## C(2) — Bank Account Smart Contract: Deposit, Withdraw, Balance

### Question / Aim
Deploy a **bank account smart contract on a test network** that supports **depositing money, withdrawing money and showing the customer's balance**.

### Theory
- A smart contract can maintain a **per-wallet balance ledger** for accounts identified by blockchain addresses.
- **Deposit:** A user sends test ETH to the contract; the contract updates that user's recorded balance.
- **Withdrawal:** A user requests some of their recorded balance; the contract verifies sufficient funds, reduces the stored balance and sends ETH back.
- **Balance enquiry:** A read-only query returns the amount recorded for the calling address.
- **Mapping:** A key-value storage structure, suitable for linking wallet addresses to account balances.
- **Wallet address:** Identifies a blockchain account. Transaction sender is used to separate customers' balances.
- **Events:** Transaction logs that help identify deposits and withdrawals in receipts or explorers.
- **Checks–Effects–Interactions:** A security pattern: validate conditions, update state, then interact with external addresses/contracts.
- **Re-entrancy:** A risk where an external contract attempts to call back during a transfer before the original operation finishes. Updating the balance before sending funds reduces this risk for the simple withdrawal pattern.
- **Testnet:** A network designed to test transactions using test ETH, not real-value ETH. **Remix VM** is a useful local simulation but is **not the same as deployment on a public test network**.

### Working / Practical Steps (Conceptual)
1. Compile and deploy the bank contract on the required test network (or first practise locally in Remix VM).
2. Deposit a small amount of **test ETH** from one wallet/account.
3. Read the recorded balance and verify that it increased.
4. Withdraw an amount smaller than the balance.
5. Read the balance again and verify that it decreased.
6. Attempt an excessive withdrawal and confirm that the transaction is rejected.
7. Observe contract address, transaction status and gas/transaction fees for the operations.

### Complexity / Key Points
- **Deposit and balance lookup:** Mapping operations are usually treated as **O(1)** at an algorithmic level. Actual gas cost depends on EVM storage operations.
- **Withdrawal:** Includes state updates and an ETH transfer; external interactions require security checks.
- **Note:** This is a **demonstration ETH ledger**, not a licensed real-world bank account or traditional banking backend.

### Viva Questions & Answers

**Q1. What is the aim of the bank smart contract?**  
**Ans:** To demonstrate deposits, withdrawals and balance enquiry through blockchain transactions.

**Q2. What is a smart contract?**  
**Ans:** Deployed blockchain code that executes its rules when called.

**Q3. What is a test network?**  
**Ans:** A blockchain network used for testing applications with non-real-value test assets.

**Q4. What is the difference between Remix VM and a public testnet?**  
**Ans:** Remix VM simulates a blockchain locally; a public testnet uses real network nodes and test ETH transactions.

**Q5. What is a mapping?**  
**Ans:** A key-value storage structure that associates each wallet address with its recorded balance.

**Q6. What is a wallet address?**  
**Ans:** A public identifier for an account used to receive or send blockchain transactions.

**Q7. What happens when a customer deposits?**  
**Ans:** Test ETH enters the contract and the customer's stored balance increases.

**Q8. What happens when a customer withdraws?**  
**Ans:** The contract verifies the balance, decreases it and transfers the requested ETH to the customer.

**Q9. Why check for sufficient balance?**  
**Ans:** To prevent withdrawing more than the account has recorded.

**Q10. Why should a withdrawal amount be positive?**  
**Ans:** A zero-value withdrawal is not meaningful and should be rejected for clear transaction rules.

**Q11. How is balance shown?**  
**Ans:** By reading the recorded balance for the calling wallet address.

**Q12. What is a read-only function?**  
**Ans:** A function that returns blockchain information without changing the contract's stored state.

**Q13. What is the purpose of events?**  
**Ans:** To log important actions so clients and explorers can inspect deposits and withdrawals.

**Q14. What is re-entrancy?**  
**Ans:** A vulnerability where an external contract re-enters an operation during an unfinished call.

**Q15. How does the contract reduce re-entrancy risk?**  
**Ans:** It checks the balance and updates internal state **before** transferring ETH outside the contract.

**Q16. What is gas in this practical?**  
**Ans:** The execution resource charge associated with deploying the contract or changing balances.

**Q17. Does checking balance cost transaction gas?**  
**Ans:** A local read-only query usually does not submit a transaction or charge the caller transaction gas; an on-chain call from another contract does consume gas.

**Q18. Why use test ETH instead of real ETH?**  
**Ans:** To test functionality without risking real funds.

**Q19. What happens if withdrawal exceeds the balance?**  
**Ans:** The transaction is rejected/reverted, so the withdrawal does not succeed.

**Q20. Is this smart contract a complete secure banking system?**  
**Ans:** No. It is an educational example; a real financial system requires extensive security, auditing, operational controls and regulatory compliance.

**Conclusion:** A bank smart contract demonstrates address-based balances and safe deposit/withdrawal rules, with transaction receipts providing testnet evidence.

---

# Last-Minute Revision Sheet

| Practical | Main concept | Most important viva points |
|---|---|---|
| **B(2)** Email Spam | KNN vs SVM | Binary labels, distance, hyperplane, precision vs recall |
| **B(3)** Bank Churn | ANN | Layers, ReLU/sigmoid, backpropagation, epochs, churn label |
| **B(4)** Diabetes | KNN evaluation | TP/TN/FP/FN, accuracy, error rate, precision, recall |
| **ML Mini-Project** Titanic | Survival classification | `Survived`, features, missing data, Random Forest, leakage |
| **C(1)** Student Data | Solidity basics | Struct, array, fallback vs receive, gas used vs gas price |
| **C(2)** Bank Account | Smart contract | Deposit, withdrawal, address mapping, balance, testnet, re-entrancy |

**Exam tip:** For every practical, prepare to answer **(1) What is the problem? (2) Which method is used? (3) How does it work? (4) Why was it chosen? (5) How is the result checked?**
