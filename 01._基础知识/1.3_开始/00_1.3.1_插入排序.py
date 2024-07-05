# 00_1.3.1_插入排序

"""
Lecture: 01._基础知识/1.3_开始
Content: 00_1.3.1_插入排序
"""

from typing import List

class InsertionSort:
    """插入排序类，提供对数组进行排序的方法。
    
    Attributes:
        data (List[int]): 待排序的整数列表。
    """
    
    def __init__(self, data: List[int]):
        """初始化插入排序类。
        
        Args:
            data (List[int]): 待排序的整数列表。
        """
        self.data = data

    def sort(self) -> List[int]:
        """对数据进行插入排序。
        
        Returns:
            List[int]: 排序后的整数列表。
        """
        n = len(self.data)
        for i in range(1, n):
            key = self.data[i]
            j = i - 1
            
            # 从已排序部分的最后一个元素开始，向前扫描并寻找插入位置
            while j >= 0 and self.data[j] > key:
                self.data[j + 1] = self.data[j]
                j -= 1
            self.data[j + 1] = key
            
            # 打印当前步骤的中间结果
            print(f"插入元素 {key} 后的数组: {self.data}")
        
        return self.data

def main():
    """主函数，用于测试插入排序功能。
    """
    # 示例数据
    data = [34, 8, 64, 51, 32, 21]
    print("原始数组: ", data)
    
    # 初始化排序类并进行排序
    sorter = InsertionSort(data)
    sorted_data = sorter.sort()
    
    # 打印排序结果
    print("排序后的数组: ", sorted_data)

if __name__ == "__main__":
    main()
