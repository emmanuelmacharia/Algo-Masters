using System;

namespace Strings_Data_structures
{
    class Program
    {
        static void Main(string[] args)
        {
            // check pangram https://www.geeksforgeeks.org/pangram-checking/


            string str = "The quick brown fox jumps over the lazy do";

            if (CheckPangram(str) == true)
                Console.WriteLine(str + " is a pangram.");
            else
                Console.WriteLine(str + " is not a pangram.");




            //// Longest subsequence
            ////https://www.geeksforgeeks.org/find-length-longest-subsequence-one-string-substring-another-string/
            ////https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

            String s1 = "AGGTAB";
            String s2 = "GXTXAYB";

            char[] X = s1.ToCharArray();
            char[] Y = s2.ToCharArray();
            int m = X.Length;
            int n = Y.Length;

            Console.Write("Length of LCS is" + " "
                        + lcs(X, Y, m, n));
        }
        public static bool CheckPangram(string str)
        {
            bool[] mark = new bool[26];

            int index = 0;
            for (int i = 0; i < str.Length; i++)
            {

                if (str[i] >= 'A' && str[i] <= 'Z')
                    index = 'Z' - str[i];
                if (str[i] >= 'a' && str[i] <= 'z')
                    index = 'z' - str[i];
                mark[index] = true;
            }
            for (int i = 0; i <= 25; i++)
                if (mark[i] == false)
                    return (false);
            return (true);

        }
        //O(n)



        static int lcs(char[] X, char[] Y, int m, int n)
        {
            if (m == 0 || n == 0)
                return 0;
            if (X[m - 1] == Y[n - 1])
                return 1 + lcs(X, Y, m - 1, n - 1);
            else
                return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n));
        }

        static int max(int a, int b)
        {
            return (a > b) ? a : b;
        }
    }
}
