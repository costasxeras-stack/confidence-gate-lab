# Case study: picking the confidence threshold for an AI classifier

Version 0.1.0 · 20 November 2026 · Data: Banking77 test set, 3,080 questions

## The question

An AI classifier reads a customer question, picks an intent and gives a confidence score. A product team then has to decide above which confidence the answer goes straight to the customer, and below which a person checks it first.

I wanted to answer three questions:

1. How much automation do you get for a given error rate, and how much does a better model change that?
2. Can a threshold chosen for one model be reused for another?
3. Is one threshold right for every kind of question?

## Approach

- Data: Banking77, a public set of bank customer questions labelled by people with one of 77 intents. 10,003 questions to train, 3,080 to test. All numbers below are on the test questions.
- Two models, trained once offline:
  - Keyword baseline: naive Bayes on word counts. Cheap and common as a first version.
  - AI classifier: sentence embeddings with logistic regression on top.
- For every threshold from 0 to 1, I counted the questions above it (answered automatically), how many of those were wrong, and how many were left for a person.
- The app lets anyone repeat this with their own error target or their own costs.

## Headline numbers

| Measure | Keyword baseline | AI classifier |
|---|---|---|
| Accuracy if every question is answered automatically | 84.4% | 87.8% |
| Share automated with at most 1% wrong (threshold) | 41.8% (0.99) | 49.8% (0.85) |
| Share automated with at most 2% wrong (threshold) | 55.1% (0.96) | 67.0% (0.72) |
| Share automated with at most 5% wrong (threshold) | 73.3% (0.82) | 83.8% (0.50) |
| Wrong answers among those with confidence 0.9 or more | 3.3% (67 of 2,032) | 0.8% (9 of 1,176) |

Source: Banking77 test set, scored 20 November 2026. Thresholds are rounded up to two decimals, as in the app, so the error rate never goes over the target.

## Findings

### 1. The better model buys automation, not just accuracy (confirmed)

If both models answered everything, the gap would look small: 84.4% against 87.8% accuracy. At a fixed 2% error rate the gap is much larger. The AI classifier answers 67.0% of questions automatically, the keyword baseline 55.1%. For a team that pays per human check, that difference is the business case, and accuracy alone hides it.

### 2. A threshold does not carry over between models (confirmed)

To stay at or under 2% wrong, the keyword baseline needs a threshold of 0.96 and the AI classifier 0.72. If a team set 0.72 for the keyword model, 6.4% of its automatic answers would be wrong instead of 2%. The keyword model is overconfident: its average confidence (0.87) is above its accuracy (0.84). The AI classifier is the opposite: average confidence 0.76, accuracy 0.88.

What this means for a product: the threshold belongs to a model version, and it has to be checked again on labelled data every time the model changes.

### 3. One threshold for all intents hides weak spots (confirmed)

At the threshold for 2% wrong (0.72), the AI classifier answers 25% of "card acceptance" questions automatically and 98% of "age limit" or "lost or stolen phone" questions. The hardest intents are close relatives, such as "topping up by card", "top up failed" and "top up reverted", or "declined transfer" and "declined card payment". A per-intent rule (never automate some intents, or use a stricter threshold for them) would likely cut errors further. I have not built or measured that yet.

### 4. Some confident mistakes are taxonomy problems, not model problems (hypothesis)

Among the AI classifier's few wrong answers with confidence 0.9 or more, several look like questions that fit two intents. For example, "How long does a card delivery take?" is labelled "card arrival", and the model answered "card delivery estimate". My hypothesis is that part of the remaining error comes from overlapping intents, so merging or redefining some intents might help more than a better model. Testing this needs a manual review of the confident mistakes.

## What I learned as a PM

- Ask "how much can we automate at the error rate we accept?", not "how accurate is the model?". The first question is the one the business pays for.
- The threshold is part of the release. A model update without a new threshold check is a silent change in risk.
- The cost of a wrong answer differs by intent. A wrong answer about card fees is not the same as a wrong answer about a compromised card.

## Limits

- One public dataset, in English, from one domain (retail banking).
- The test questions are clean single questions. Real customer messages are longer, messier and sometimes ask two things.
- The thresholds are found on the same test set they are reported on. A real launch should choose the threshold on one labelled set and confirm it on fresh data.
- The two models are small and run offline. A large language model would have different confidence behaviour. That is a next step, not a result here.

## What I would do next

1. Choose thresholds on a validation split and report on the test split only.
2. Add per-intent thresholds and measure the gain against one global threshold.
3. Review the confident mistakes by hand to test the overlapping-intents hypothesis.
4. Add a large language model as a third classifier, and compare its confidence with how often it is right.
