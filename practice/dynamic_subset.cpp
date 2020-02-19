#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

static int total_nodes;
void printValues(std::vector<int> A, int size){
   for (int i = 0; i < size; i++) {
      printf("%*d", 5, A[i]);
   }
   printf("\n");
}
int subset_sum(std::vector<int>& s, std::vector<int>& t, int s_size, int t_size, int sum, int ite, int const target_sum){
   total_nodes++;
   if (target_sum == sum) {
       std::vector<int> copy = t;
       return t_size;
        // printValues(t, t_size);
       subset_sum(s, t, s_size, t_size - 1, sum - s[ite], ite + 1, target_sum);
    //    return;
   }
   else {
      for (int i = ite; i < s_size; i++) {
         t[t_size] = s[i];
         int found = subset_sum(s, t, s_size, t_size + 1, sum + s[i], i + 1, target_sum);
         if (found) return found;
      }
   }
   return 0;
}
std::vector<int> generateSubsets(std::vector<int>& s, int size, int target_sum){
//    int* tuplet_vector = (int*)malloc(size * sizeof(int));
   std::vector<int> tuplet_vector(size);
   int found_size = subset_sum(s, tuplet_vector, size, 0, 0, 0, target_sum);
   tuplet_vector.resize(found_size);
   return tuplet_vector;

   //    free(tuplet_vector);
}

PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("add", &generateSubsets, "A function which adds two numbers");
}
// int main(){
//    int set[] = { 5, 6, 12 , 54, 2 , 20 , 15 };
//    int size = sizeof(set) / sizeof(set[0]);
//    printf("The set is ");
//    printValues(set , size);
//    generateSubsets(set, size, 25);
//    printf("Total Nodes generated %d\n", total_nodes);
//    return 0;
// }