class Solution:
    def addBinary(self, a: str, b: str) -> str:
        try:
            result, carry_forward = "", 0
            """
            Make sure a and b are of the same length so that only one loop can be
            used to access characters of both of the strings.
            """
            if len(a) > len(b):
                b = b.zfill(len(a))
            elif len(a) < len(b):
                a = a.zfill(len(b))

            for i in range(len(a) - 1, -1, -1):
                if (
                    int(a[i]) == 1
                    and int(b[i]) == 0
                    or int(a[i]) == 0
                    and int(b[i]) == 1
                ):
                    if carry_forward:
                        result += str(0)
                        carry_forward = 1
                    else:
                        result += str(1)
                elif int(a[i]) == 0 and int(b[i]) == 0:
                    if carry_forward:
                        result += str(1)
                    else:
                        result += str(0)
                    carry_forward = 0
                elif int(a[i]) == 1 and int(b[i]) == 1:
                    if carry_forward:
                        result += str(1)
                    else:
                        result += str(0)
                    carry_forward = 1

            result += str(carry_forward) if carry_forward else ""

            return result[::-1]

        except Exception as e:
            print(e)


if __name__ == "__main__":
    obj = Solution()
    print(obj.addBinary("0", "0"))
