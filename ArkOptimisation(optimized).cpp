#define sizen 4
#include <bits/stdc++.h>
#include <iostream>

using namespace std;

long long costMatrixA[sizen][sizen];
long long costMatrixB[sizen][sizen];

long long productMat[sizen][sizen];

long long dpMin[sizen][sizen] = {0};
long long dpMax[sizen][sizen] = {0};

//Simple recursion  which returns the minimum cost of going from i,j to n,n
// long long FindMinCostA(int i, int j, int n)
// {
//     //going out of bounds
//     if (i >= n)
//         return INT_MAX;
//     //going out of bounds
//     if (j >= n)
//         return INT_MAX;
//     //reaching the last cell
//     if (i == n - 1 && j == n - 1)
//         return costMatrixA[i][j];
//     //going down or right
//     return costMatrixA[i][j] + min(FindMinCostA(i + 1, j, n), FindMinCostA(i, j + 1, n));
// }

long long FindMinCostA(int n1, int n2, int n)
{
    if (dpMin[n1][n2])
        return dpMin[n1][n2];

    if (n1 >= n || n2 >= n)
        return INT_MAX;
    
    if (n1 == n - 1 && n2 == n - 1)
        return costMatrixA[n1][n2];

    dpMin[n1][n2] = costMatrixA[n1][n2] + min(FindMinCostA(n1 + 1, n2, n), FindMinCostA(n1, n2 + 1, n));
    return dpMin[n1][n2];
}

//Simple recursion which returns the maximum cost of going from i,j to n,n
// long long FindMaxCostB(int i, int j, int n)
// {
//     //going out of bounds
//     if (i >= n)
//         return 0;
//     //going out of bounds
//     if (j >= n)
//         return 0;
//     //reaching the last cell
//     if (i == n - 1 && j == n - 1)
//         return costMatrixB[i][j];
//     //going down or right
//     return costMatrixB[i][j] + max(FindMaxCostB(i + 1, j, n), FindMaxCostB(i, j + 1, n));
// }

long long FindMaxCostB(int n1, int n2, int n)
{
    if (dpMax[n1][n2])
        return dpMax[n1][n2];

    if (n1 >= n || n2 >= n)
        return 0;
    
    if (n1 == n - 1 && n2 == n - 1)
        return costMatrixB[n1][n2];

    dpMax[n1][n2] = costMatrixB[n1][n2] + max(FindMaxCostB(n1 + 1, n2, n), FindMaxCostB(n1, n2 + 1, n));
    return dpMax[n1][n2];
}

int main()
{
    int i, j, k;
    srand(time(0));
    // initialisation
    for (i = 0; i < sizen; i++)
    {
        for (j = 0; j < sizen; j++)
        {
            costMatrixA[i][j] = 1 + rand() % 10;
            costMatrixB[i][j] = 1 + rand() % 10;
            productMat[i][j] = 0;
        }
    }
    //creating productMat as explained in the beginning
    for (i = 0; i < sizen; i++)
    {
        for (j = 0; j < sizen; j++)
        {
            for (k = 0; k < sizen; k++)
                productMat[i][j] += FindMinCostA(i, k, sizen) * FindMaxCostB(k, j, sizen);
        }
    }
    //filter of size 4 x n
    long long filterArray[4][sizen];
    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < sizen; j++)
            filterArray[i][j] = rand() % 2;
    }
    // matrix of dimension (sizen/c) x 1 where c = 4
    long long finalMat[sizen / 4];
    // applying the filter
    for (i = 0; i < sizen - 4; i += 4)
    {
        long long sum = 0;
        // dot product of 4xn portion of productMat
        for (j = 0; j < sizen; j++)
        {
            for (int filterRow = 0; filterRow < 4; filterRow++)
            {
                sum += productMat[i + filterRow][j];
            }
        }
        finalMat[i / 4] = sum;
    }

    return 0;
}