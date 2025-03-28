# **Step-by-Step by guide for Question 06_Print_Divisor**

# **Finding Divisors of a Number (Example: 20)**

## **How It Works**
To find divisors of a number **N**, we check every number from **1 to N** and see if it divides **N** without leaving a remainder.

---

## **Step-by-Step Execution of Loop (N = 20)**

| `i`  | `20 % i` | Remainder | **Divisor?** |
|------|---------|----------|------------|
| 1    | 20 ÷ 1  | 0        | ✅ Yes (Print 1) |
| 2    | 20 ÷ 2  | 0        | ✅ Yes (Print 2) |
| 3    | 20 ÷ 3  | **2**    | ❌ No |
| 4    | 20 ÷ 4  | 0        | ✅ Yes (Print 4) |
| 5    | 20 ÷ 5  | 0        | ✅ Yes (Print 5) |
| 6    | 20 ÷ 6  | **2**    | ❌ No |
| 7    | 20 ÷ 7  | **6**    | ❌ No |
| 8    | 20 ÷ 8  | **4**    | ❌ No |
| 9    | 20 ÷ 9  | **2**    | ❌ No |
| 10   | 20 ÷ 10 | 0        | ✅ Yes (Print 10) |
| 11   | 20 ÷ 11 | **9**    | ❌ No |
| 12   | 20 ÷ 12 | **8**    | ❌ No |
| 13   | 20 ÷ 13 | **7**    | ❌ No |
| 14   | 20 ÷ 14 | **6**    | ❌ No |
| 15   | 20 ÷ 15 | **5**    | ❌ No |
| 16   | 20 ÷ 16 | **4**    | ❌ No |
| 17   | 20 ÷ 17 | **3**    | ❌ No |
| 18   | 20 ÷ 18 | **2**    | ❌ No |
| 19   | 20 ÷ 19 | **1**    | ❌ No |
| 20   | 20 ÷ 20 | 0        | ✅ Yes (Print 20) |

---

## **Final Output**
