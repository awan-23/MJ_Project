#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// Missing Integer 
int missing_int(int A[], int N) {
    // write your code in C99 (gcc 6.2.0)
    // pigeon-hole principle...

    // set up candidates
    int candidates[N+1];
    int min = N+1;
    for (int i = 0; i <= N; i++) {
        candidates[i] = i;
    }
    
    // if candidate is in A, set it to max number
    for (int i = 0; i < N; i++) {
    	int entry = A[i];
    	if (entry > 0 && entry < min) {
    		candidates[A[i]] = N+1;
    	}
    }
    
    // find minimum
    for (int i = 1; i <= N; i++) {
    	int next = candidates[i];
    	if (next < min) {
    		min = next;
    	}
    }
    
    return min;
}


int counter(char S[]){
	int current_max = 0;
	bool word = false;  // has a word been started already?
	int count = 0;  // how many words in the sentence so far?
	int length = strlen(S);
	char punctuation[] = " .!?";
	for (int i = 0; i < length; i++) {
		char ch = S[i];
		if (strchr(punctuation, ch)) {
			if (word) {
				count++;
			}
			word = false;
			if (ch != ' ') {
				if (count > current_max) current_max = count;
				count = 0;
			}
		} else {
			word = true;
		}
	}
	if (word) {
		count++;
		if (count > current_max) current_max = count;
	}
	return current_max;
}


// from https://stackoverflow.com/questions/15094834/check-if-a-value-exist-in-a-array
bool isvalueinarray(int val, int *arr, int size){
    int i;
    for (i=0; i < size; i++) {
        if (arr[i] == val)
            return true;
    }
    return false;
}

// Cost minimizer
int cost_minimizer(int A[], int n) {
	int last_day = A[n-1];
	int memo[last_day+1];
	for (int i = 0; i < last_day+1; i++) {
		if (isvalueinarray(i, A, n)) {
			memo[i] = 1;
		} else {
			memo[i] = 0;
		}
	}

	for (int i = 0; i < last_day+1; i++)
		if (memo[i] == 0) {
			memo[i] = memo[i-1];
		} else {
			int before29 = 0;
			int before6 = 0;
			if (i-29 > 0) {
				before29 = i-29;
			}
			if (i-6 > 0) {
				before6 = i-6;
			}

			int curr_cheapest = memo[i-1] + 2;
			int sevenday = memo[before6] + 6;
			int thirtyday = memo[before29] + 25;

			//printf("%d, %d, %d\n", curr_cheapest, sevenday, thirtyday);

			if (curr_cheapest > sevenday) curr_cheapest = sevenday;
			if (curr_cheapest > thirtyday) curr_cheapest = thirtyday;


			memo[i] = curr_cheapest;

		}

	return memo[last_day-1];



}



// maximal sum-distance value
int solution(int A[], int N) {
	// want the largest values
	// at the smallest and highest indices.

	// if the i'th element is selected as P,
	// it contributes A[i] - i to the sum-distance.
	// if selected as Q,
	// it contributes A[i] + i.

	// traverse array from both ends:
	// value of low_max i = A[i] - i
	// value of high_max j = A[j] + j
	int low_max = 0;
	int high_max = 0;

	int i;
	int j;
	for (i = 0, j = N-1; i <= N; i++, j--) {
		int low_element = A[i] - i;
		int high_element = A[j] + j;
		if (low_max < low_element) low_max = low_element;
		if (high_max < high_element) high_max = high_element;

	}

	return low_max + high_max;

}






int main(){

	printf("testing missing_int\n");
	int test[] = {3, 2, 1, 5, 6, 7};
	printf("test: %d\n", missing_int(test, 6));

	int test2[] = {0};
	printf("test2: %d\n", missing_int(test2, 1));

	int test3[] = {1};
	printf("test3: %d\n", missing_int(test3, 1));


	printf("testing word counter\n");
	char count_test[] = "Hello a a a a. This is a    test       t t t t t. Heh!";
	printf("count_test: %d\n", counter(count_test));

	char count_test2[] = ". . x . x x x . x x x x   x";
	printf("count_test2: %d\n", counter(count_test2));


	printf("testing cost minimizer\n");
	int cost_test[] = {1, 2, 4, 5, 7, 29, 30};
	printf("cost_test: %d\n", cost_minimizer(cost_test, 7));


	return 0;
}


















