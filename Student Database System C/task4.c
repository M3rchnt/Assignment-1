/*
Note: If the program fails to run from VSCode please run the executable application located in the folder.
*/


#include <stdio.h> // Imports
#include <stdlib.h>
#include <string.h>
int i = 0; // Initialize counter for specific student indexes
void addStudent(); // Initialize functions used
void displayAllStudents();
void displayStudentByID(int input);

struct students{ // Initialize students structure
    char name[30];
    int age;
    int ID;
} student[500];

void addStudent(){ // Function used when adding a new student
   printf("\nAdd the Student's Details\n\n");
   printf("Enter the name of the student (max 30 characters):\n");
   scanf("%s", student[i].name);
   printf("Enter the age of the student:\n");
   scanf("%d", &student[i].age);
   printf("Enter the ID of the student:\n");
   scanf("%d", &student[i].ID);
   i += 1;
}

void displayAllStudents(){ // Function used to display all student data
    printf("\nDisplaying All Student Data...\n");
    for (int j = 0; j < i; j++) {
        printf("Student Name: %s\nStudent Age: %d\nStudent ID: %d\n\n", student[j].name, student[j].age, student[j].ID);
    }
}

void displayStudentByID(int input){ // Function used to display a specific student's data depending on a given ID
    int j = 0;
    while ((j < i) && (student[j].ID != input)){
        j += 1;
    }
    if (j != i) {
        printf("\nStudent Name: %s\nStudent Age: %d\nStudent ID: %d\n", student[j].name, student[j].age, student[j].ID);
    }
    else {
        printf("\nStudent not found\n");
    }
}

int main() {
    int decision = 1;
    while (decision > 0) { // Core loop that runs for testing purposes. 
        printf("\nEnter a number for the task you would like to perform: \n");
        printf("1. Create New Student Data (max 500 students)\n");
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
    return 0;
}
