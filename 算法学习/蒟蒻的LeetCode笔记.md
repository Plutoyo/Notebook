### 刷LeetCode

思考20分钟,若完全无思路就去学习

### 动态规划

+ [53. 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)

​		因为要求是最大的连续子序列,所以一定需要维护的f[i]第i位要在数组中,不然没办法递推下去,这是动态规划需要考虑的问题

+ [面试题 17.16. 按摩师](https://leetcode-cn.com/problems/the-masseuse-lcci/) 

  ​		按摩师需要进行状态转移的维护,因为不能连续的接受预约,所以需要对上一次的状态进行维护,一个是第i次接受了预约,一个是第i次没有接受预约,要分清状态的情况来进行讨论,联想到之前看到的状态压缩dp,他使用了二进制位来表示不同的状态,这里的状态较少,所以使用二维数组就能维护,第一维代表到第i的最大预约时间,第二个维度0和1分别代表了第i次接受预约和第i次不接受预约.

  ​		如果是有更多的状态,在第二维可以开更大的数组来表示状态,但是如果状态实在是太过于多,就可以考虑状态压缩的二进制位来表示~~(我好菜不会位运算)~~

> 算法改良:
>
> 由于只需要维护2个状态0与1,所以不需要开数组,t=0,0=max(0,1);1=t+nums[i];

+ #### [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)

  动态规划只能考虑走一步的情况,如果必须要考虑多步可能就会出现错误

+ #### [392. 判断子序列](https://leetcode-cn.com/problems/is-subsequence/)

  ~~万物基于DP(bushi)~~这道题也能DP是没想到的,通过对字符串进行DP

  使用 $$ f( i , j )  $$表示从第$$ i$$ 个位置往后,  $$j$$  字符出现的位置
  $$
  f(i,j)=
  \begin{cases}
  	i & \text{j=t[i]}\\
  	f(i+1,j) & \text{j$\neq$t[i]} 
  \end{cases}
  $$
  因为是全是小写字母,所以使用第二维来表示ASCII码,因为全是小写字母,所以只需要开26大小,使用c-'a'来映射

  对于检查的时候,使用

  ```C++
  for(int i=0;i<s.size();i++)
  {
      if(dp[k][s[i]-'a']!=t.size())
      {
          k=dp[k][s[i]-'a']+1;
          //因为如果dp[k][s[i]-'a']满足条件,那么这个里面就存的是从k开始满足条件的字符,所以当这个字符匹配到之后,需要往后跳转一位.
          cout<<k<<' ';
      }
      else return 0;
  }
  return 1;
  ```

+ [746. 使用最小花费爬楼梯](https://leetcode-cn.com/problems/min-cost-climbing-stairs/)

   	*dp*[*i*]=min(*dp*[*i*−1]+*cost*[*i*−1],*dp*[*i*−2]+*cost*[*i*−2]) 

  dp[i]代表第i层时所花费的最小代价,由于能够跨一层或者两层,所以需要考虑是从$$dp[i-1]$$转移来还是$$dp[i-2]$$转移来
  
+ #### [剑指 Offer 58 - II. 左旋转字符串](https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/)

   记住字符串取子串函数s.substr(起始位置,长度)

   ```C++
   string substr (size_t pos = 0, size_t len = npos) const;
   ```