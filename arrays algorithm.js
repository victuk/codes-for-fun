// arrays

// numbers = [1, 2, 3, 4, 5] ----> 5
// numbers.length - array property to find out the length of an array or string.

// Array.isArray(numbers) ----> true
// num = 5;
// Array.isArray(num) ----> false
// Array.isArray(<argument>) checks if a variable is an array
// or if a function returns an array.

// var nums = [];
// for (var i = 0; i < 10; ++i) {
// nums[i] = i+1;
// }

// var numbers = [1,2,3,5,8,13,21];
// var sum = 0;
// for (var i = 0; i < numbers.length; i++) {
// sum += numbers[i];
// }
// console.log(sum);

// name = ["Cynthia", "Morgan", "Kelechi", "Uduak"]
// name.indexOf("Morgan") ----> 1
// name.indexOf("Wilson") ----> -1
// indexOf() is used to get the index of an element 
// in an Array, if the element dosen't exist in the array, -1 will be returned.
// lastIndexOf() is used to find out the last index of the argument.
// name.join() used to join an array into a single string and seperates by a comma by default.
// name.join(" ") seperates joins an array and seperates it by space (which is its argument).


// var itDiv = ["Mike","Clayton","Terrill","Raymond","Cynthia","Danny","Jennifer"];
// var dmpDept = itDiv.splice(3,3);
// var cisDept = itDiv;
// console.log(dmpDept); ----> Raymond,Cynthia,Danny
// console.log(cisDept); ---->Mike,Clayton,Terrill,Jennifer

// Splice can also be used for adding and removing elementd in an array.
// var nums = [1,2,3,7,8,9];
// nums.splice(3,0,4,5,6);
// console.log(nums); ----> 1, 2, 3, 4, 5, 6, 7, 8, 9
// var nums = [1,2,3,100,200,300,400,4,5];
// nums.splice(3,4);
// console.log(nums); ----> 1,2,3,4,5;

// var nums = [1,2,3,4,5];
// console.log(nums); ----> 1,2,3,4,5
// nums[nums.length] = 6;
// console.log(nums); ----> 1,2,3,4,5,6

// var nums = [2,3,4,5];
// console.log(nums); ----> 2,3,4,5
// var newnum = 1;
// nums.unshift(newnum);
// console.log(nums); ----> 1,2,3,4,5
// unshift() is used to add elements to the beginning of an array.
// unshift accepts multiple arguments.

// shift is used to remove an element at the beginning of an array.

// array.pop removes an element at the end of an array.

// reversing an Array
// var nums = [1,2,3,4,5];
// nums.reverse();
// console.log(nums); ----> 5,4,3,2,1

// Sorting an array
// var names = ["David","Mike","Cynthia","Clayton","Bryan","Raymond"];
// names.sort();
// console.log(names); ----> Bryan,Clayton,Cynthia,David,Mike,Raymond;

// Sort numbers
// var nums = [3,1,2,100,4,200];
// nums.sort();
// console.log(nums); ----> 1,100,2,200,3,4;
// As we can see, this didint Worker, a way to eficiently sort numbers
// will be::::::
// function compare(num1, num2) {
//     return num1 - num2;
//     }
//     var nums = [3,1,2,100,4,200];
//     nums.sort(compare);
//     console.log(nums); ----> 1,2,3,4,100,200

// Iterating through numbers
// function square(num) {
//     print(num, num * num);
//     }
//     var nums = [1,2,3,4,5,6,7,8,9,10];
//     nums.forEach(square);