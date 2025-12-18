---
layout: post
title: "1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance"
date: 2025-12-11 00:32:11 +0900
categories: [Algorithm, Leetcode]
tags: [dp]
---

[Find the City With the Smallest Number of Neighbors at a Threshold Distance - LeetCode](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/)

```java
import java.util.*;

class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        
        int e = edges.length;

        int[][] dist_dp = new int[n][n];
        
        
        // 초기화
        for (int i = 0; i < n; i++) {
            // 오버플로우 조심
            Arrays.fill(dist_dp[i], 100001);
            dist_dp[i][i] = 0;
        }

        // w로 채우기
        for(int i=0; i<edges.length; i++){
                int a = edges[i][0];
                int b = edges[i][1];
                int w = edges[i][2];

                dist_dp[a][b] = w;
                dist_dp[b][a] = w;
        }        

        // 플로이드 워셜로 경로 최솟값 업데이트
        for(int k=0; k<n; k++){
            for (int i=0; i<n; i++){
                for(int j=0; j<n; j++){

                    if(dist_dp[i][k] + dist_dp[k][j] < dist_dp[i][j]){
                        dist_dp[i][j] = dist_dp[i][k] + dist_dp[k][j];
                    }
                }
            }
        }

        // 노드마다 가는 길 카운트하고, 
        // 최소카운트면, 답 노드 최댓값으로 
        int minReachable = Integer.MAX_VALUE;
        int ans = 0;
        for (int i=0; i<n;i++){
            int count = 0;

            for(int j=0; j<n; j++){
                if(i!=j && dist_dp[i][j] <= distanceThreshold){
                    count ++;
                }
            }
            if (count <= minReachable){
                minReachable = count;
                ans = i;
            }
        }
        
        return ans;
        
    }
}
```

- 초기화할때 Integer.MAX_VALUE 오버플로우나서 오류 → 10001로 수정