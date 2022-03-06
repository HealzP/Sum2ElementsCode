class sum2element():
   def towsum(self, nums, target):
      required = {}
      for i in range(len(nums)):
         if target - nums[i] in required:
            return [required[target - nums[i]],i]
         else:
            required[nums[i]]=i

input_list1 = [2, 7, 11, 15]
sun_target1 = 9

input_list2 = [3, 2, 4]
sun_target2 = 6

input_list3 = [3, 1, 2, 3]
sun_target3 = 6

input_list4 = [3, 2]
sun_target4 = 6

check_output = sum2element()

print("Output = ",check_output.towsum(input_list1, sun_target1),"Because nums[0] + nums[1] = 9")
print("Output = ",check_output.towsum(input_list2, sun_target2),"Because nums[1] + nums[2] = 6")
print("Output = ",check_output.towsum(input_list3, sun_target3),"Because nums[0] + nums[3] = 6")
print("Output = ",check_output.towsum(input_list4, sun_target4),"The are no two numbers that add up to 3")