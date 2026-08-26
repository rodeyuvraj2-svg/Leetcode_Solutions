int removeDuplicates(int* nums, int numsSize) {
    int left = 0, right = 1;

    if (numsSize == 0) {
        return 0;
    }

    while (right < numsSize) {
        if (nums[left] == nums[right]) {
            right ++;
        }
        else {
            left ++;
            nums[left] = nums[right];
            right ++;
        }
    }
    return left + 1;
}