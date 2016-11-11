#coding=utf-8

'''
找到[1..n]数组中重复的数字或不在1~n区间内的 "一个" 数字


可以通过排序和hash的方式来找到重复或不在[1..n]区间内的数字，但都不是最优的算法，从空间复杂度和时间复杂度两个维度来梳理下这个算法：
1.通过二分法排序一个队列，需要的时间复杂度是O(nlogn)，空间复杂度是O(1)
2.通过hash的方式，因为需要开辟一个和数组大小一样的空间，而且需要和数组大小一致的hash比对次数，所以时间复杂度和空间复杂度都是O(n)


可以从另外一个思路来实现这个算法，就是把数字换到对应的位置上面去，比如数组[3,1,7,8,6,5,2,4,6]：
1.当遍历到nums[0]时，发现数字3，然后可以把3换到nums[3-1]上面，把nums[3-1]上的数字7换到nums[0]上；
2.然后发现nums[0]上的数字是7，然后把7换到nums[7-1]上面，把nums[7-1]上的数字2换到nums[0]上；
3.然后发现nums[0]上的数字是2，然后把2换到nums[2-1]上面，把nums[2-1]上的数字1换到nums[0]上；
4.以此类推，指到发现重复数字6，或者是超出n或小于1的数字
该算法的时间复杂度为O(n)，空间复杂度为O(1)

'''


def  find_special_num(nums):
    '''
    找到[1..n]数组中重复的数字或不在1~n区间内的 "一个" 数字
    n为len(nums)-1
    '''
    print '===',nums,'==='
    n = len(nums) -1
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


if __name__ == "__main__":
    nums = [3,10,7,8,6,5,2,4,6] # [3,10,7,8,6,5,2,4,6]
    print find_special_num(nums)


