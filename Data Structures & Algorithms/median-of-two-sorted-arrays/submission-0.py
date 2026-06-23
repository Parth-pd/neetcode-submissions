class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = B, A
        
        l, r = 0, len(A) - 1

        total = len(A) + len(B)
        half = total // 2

        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if i < len(A) - 1 else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if j < len(B) - 1 else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    ans = (max(Aleft,Bleft) + min(Aright,Bright)) / 2
                    return ans
            
            if Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        