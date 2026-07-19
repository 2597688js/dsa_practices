# Greedy Algorithm

> ⚠️ A greedy algorithm does **not** guarantee the optimal solution for every problem.

## What is a Greedy Algorithm?

A **greedy algorithm** always makes the best possible choice at the current moment, hoping that these local optimal choices will eventually lead to the overall optimal solution.

Think of it like this:

> **"I won't worry about the future. I'll simply choose the best option available right now."**

Once a decision is made, a greedy algorithm **never goes back** to change it.

---

## Example

Suppose you need to make **₹93** using the following denominations:

- ₹50
- ₹20
- ₹10
- ₹5
- ₹2
- ₹1

### Greedy Approach

At each step, choose the **largest denomination** that does not exceed the remaining amount.

| Step | Chosen Note/Coin | Remaining Amount |
|------|------------------:|-----------------:|
| 1 | ₹50 | ₹43 |
| 2 | ₹20 | ₹23 |
| 3 | ₹20 | ₹3 |
| 4 | ₹2 | ₹1 |
| 5 | ₹1 | ₹0 |

So, the selected denominations are:

```
50 → 20 → 20 → 2 → 1
```

---

## How a Greedy Algorithm Thinks

For every decision, it asks:

1. Which option looks **best right now**?
2. Choose that option.
3. Move forward.
4. Never reconsider previous choices.

In short:

> **Choose the best now, hope it's best overall.**