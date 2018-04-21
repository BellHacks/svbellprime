(function(){
var a =20
if(true){
    let a =10
    console.log(a)
}
console.log(a)
var ar =[]
for(var i=0; i <4; i++){
    ar.push(function(){
        console.log(i)
    })

}
ar[0]()
ar[1]()
for(let i=0; i <4; i++){
    ar.push(function(){
        console.log(i)
    })

}
ar[0]()
ar[1]()
})()