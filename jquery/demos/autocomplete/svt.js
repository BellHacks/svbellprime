Function.prototype.bind = Function.prototype.bind  || function(context){
	var self = this;
	return function(){
		return self.apply(context, arguments)
	}
}

function isTwoPassed(){
	let n =2;
	console.log(arguments);
	var ar = Array.prototype.slice.call(arguments);
	console.log(ar);
 return 	ar.indexOf(n) > 0


}

isTwoPassed(1,4,5)

let d = new Date(2018,1,29,11,12,13)
d.toString()

Math.max.apply(null, arr)

function prefix(){
	let n =2;
	console.log(arguments);
	var ar = Array.prototype.slice.call(arguments);
	ar.unshift('sv')
	console.log(ar);
 return 	ar


}

a=2
function b(){
	a=10;
  return;
	var a = function(){}
}

var a = 1; 
function b() { 
    a = 10; 
    return; 
    function a() {} 
} 

for(var i = 0; i < 10; i++) {
    setTimeout(function() {
      console.log(i);  
    }, 10);
}



for(var i = 0; i < 10; i++) {
    setTimeout((function(i){
	console.log(i)
})(i), 10);
}


for(var i = 0; i < 10; i++) {
    setTimeout((function(i) {
      console.log(i);
    })(i), 10)
}

for(var i=0; i <10; i++){
	setTimeout(function(){
		console.log.bind(console,i)
	}, 10)
	
}
