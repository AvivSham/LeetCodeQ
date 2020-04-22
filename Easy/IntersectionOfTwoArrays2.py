from collections import Counter

def intersect(nums1,nums2):
    ans=[]
    if nums1 <= nums2:
        bigger = Counter(nums1)
        smaller = nums2
    else:
        bigger = Counter(nums2)
        smaller = nums1

    for num in smaller:
        if bigger.get(num) > 0:
            bigger[num] -= 1
            ans.append(num)

    return ans

if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(intersect(nums1, nums2))