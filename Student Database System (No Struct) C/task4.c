/*
Note: If the program fails to run from VSCode please run the executable application located in the folder.
*/

#include <stdio.h> // Imports
#include <stdlib.h>
#include <string.h>
int i = 0; // Initialize counter for specific student indexes
int* studentID;
int* studentAge;
char ***studentName;
size_t studentSize = 5;
void addStudent(); // Initialize functions used
void displayAllStudents();
void displayStudentByID(int input);

void addStudent(){ // Function used when adding a new student
   printf("\nAdd the Student's Details\n\n");
   printf("Enter the name of the student:\n");
   scanf("%s", &studentName[i]);
   printf("Enter the age of the student:\n");
   scanf("%d", &studentAge[i]);
   printf("Enter the ID of the student:\n");
   scanf("%d", &studentID[i]);
   i += 1;
   studentSize += 1;
   studentID = realloc(studentID, studentSize * sizeof(int));
   studentAge = realloc(studentAge, studentSize * sizeof(int));
   studentName = realloc(studentName, studentSize * sizeof(char*));
}

void displayAllStudents(){ // Function used to display all student data
    printf("\nDisplaying All Student Data...\n");
    for (int j = 0; j < i; j++) {
        printf("Student Name: %s\nStudent Age: %d\nStudent ID: %d\n\n", &studentName[j], studentAge[j], studentID[j]);
    }
}

void displayStudentByID(int input){ // Function used to display a specific student's data depending on a given ID
    int j = 0;
    while ((j < i) && (studentID[j] != input)){
        j += 1;
    }
    if (j != i) {
        printf("Student Name: %s\nStudent Age: %d\nStudent ID: %d\n\n", &studentName[j], studentAge[j], studentID[j]);
    }
    else {
        printf("\nStudent not found\n");
    }
}

int main(){
    studentID = calloc(studentSize, sizeof(int)); // Initialize arrays
    studentAge = calloc(studentSize, sizeof(int));
    studentName = calloc(studentSize, sizeof(char*));
    int decision = 1;
    while (decision > 0) { // Core loop that runs for testing purposes. 
        printf("\nEnter a number for the task you would like to perform: \n");
        printf("1. Create New Student Data\n");
        printf("2. Search for specific student data by ID\n");
        printf("3. Display all student data\n");
        printf("0. End Program\n");
        scanf("%d", &decision);
        if (decision == 1) {
            addStudent();
        }
        else if (decision == 2) {
            int inputID; 
            printf("Enter the ID of the student you are searching for: \n");
            scanf("%d", &inputID);
            displayStudentByID(inputID);
        }
        else if (decision == 3) {
            displayAllStudents();
        }
    }
    free(studentID);
    free(studentAge);
    free(studentName);
    return 0;
} 