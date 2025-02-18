class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1:
                match s[i]:
                    case "I":
                        if s[i + 1] == "V":
                            number += 4
                            i += 2
                        elif s[i + 1] == "X":
                            number += 9
                            i += 2
                        else:
                            number += 1
                            i += 1
                    case "V":
                        number += 5
                        i += 1
                    case "X":
                        if s[i + 1] == "L":
                            number += 40
                            i += 2
                        elif s[i + 1] == "C":
                            number += 90
                            i += 2
                        else:
                            number += 10
                            i += 1
                    case "L":
                        number += 50
                        i += 1
                    case "C":
                        if s[i + 1] == "D":
                            number += 400
                            i += 2
                        elif s[i + 1] == "M":
                            number += 900
                            i += 2
                        else:
                            number += 100
                            i += 1
                    case "D":
                        number += 500
                        i += 1
                    case "M":
                        number += 1000
                        i += 1
            else:
                match s[i]:
                    case "I":
                        number += 1
                        i += 1
                    case "V":
                        number += 5
                        i += 1
                    case "X":
                        number += 10
                        i += 1
                    case "L":
                        number += 50
                        i += 1
                    case "C":
                        number += 100
                        i += 1
                    case "D":
                        number += 500
                        i += 1
                    case "M":
                        number += 1000
                        i += 1
        return number


solution = Solution()
result = solution.romanToInt(s="MCMXCIV")
print(result)
