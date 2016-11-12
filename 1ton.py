#coding=utf-8

'''
找到[1..n]数组中重复的数字或不在1~n区间内的 "一个" 数字
注：1..n为连续数字，步长为1


方法1.通过二分法排序一个队列，需要的时间复杂度是O(nlogn)，空间复杂度是O(1)
方法2.通过hash的方式，因为需要开辟一个和数组大小一样的空间，而且需要和数组大小一致的hash比对次数，所以时间复杂度和空间复杂度都是O(n)


方法3：把数字换到对应的位置上面去，比如数组[3,1,7,8,6,5,2,4,6]：
1.当遍历到nums[0]时，发现数字3，然后可以把3换到nums[3-1]上面，把nums[3-1]上的数字7换到nums[0]上；
2.然后发现nums[0]上的数字是7，然后把7换到nums[7-1]上面，把nums[7-1]上的数字2换到nums[0]上；
3.然后发现nums[0]上的数字是2，然后把2换到nums[2-1]上面，把nums[2-1]上的数字1换到nums[0]上；
4.以此类推，指到发现重复数字6，或者是超出n或小于1的数字
该算法的时间复杂度为O(n)，空间复杂度为O(1)


方法4：通过1+2+3+...n = n*(n+1)/2的等式来查找连续数字中的重复数字，时间复杂度为O(n)，空间复杂度为O(1)

下面是方法3和方法4的具体实现
'''


def find_special_num3(nums):
    '''
    找到[1..n]数组中重复的数字或不在1~n区间内的 "一个" 数字

    算法思路：把数字换到与下标一致的位置上，当发现对应位置已经有正确数字时，则该数字为重复数字
    该算法的时间复杂度为O(n)，空间复杂度为O(1)
    '''
    print '===',nums,'==='
    n = len(nums) - 1 # 数组长度，-1=去除重复值或不在区间内值的占位长度
    for index,num in enumerate(nums):
        # 如果num不在1~n区间，则跳出
        if num > n or num < 1: 
            return num 
        # 把数字放到和索引一致的位置上
        while num-1 != index: 
            if num > n or num < 1 or nums[num-1] == num: # 如果对应位置已经有相同的数字或数字不在1~n区间，则跳出
                return num
            nums[num-1],nums[index] = nums[index],nums[num-1] # 互换位置
            num = nums[index] # 更新当前位置数据
            print index,nums


def find_special_num4(nums):
    '''
    找到[1..n]数组中重复的数字或不在1~n区间内的 "一个" 数字

    算法思路：通过1+2+3+...n = n*(n+1)/2的等式来查找连续数字中的重复数字；并剔除不在区间内的数字
    该算法的时间复杂度为O(n)，空间复杂度为O(1)
    '''
    n = len(nums) - 1 # 数组长度，-1=去除重复值或不在区间内值的占位长度
    n_sum = n*(n+1)/2 # 无重复数据时的累计值
    for num in nums:
        # 如果num不在1~n区间，则跳出
        if num>n or num<1:
            return num
        # 从无重复数字的累计中减去现有数据
        n_sum -= num
    return abs(n_sum) # 返回重复值



if __name__ == "__main__":
    #nums = [3,10,7,8,6,5,2,4,6] # case 1
    nums = [3,1,7,8,6,5,2,4,6] # case 2
    print find_special_num3(nums)
    print find_special_num4(nums)


