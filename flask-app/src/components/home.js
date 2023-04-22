import { useState,useEffect } from "react";
function Home(){
      const ENDPOINT = "http://127.0.0.1:5000";
      const [namee,setName]=useState("")
    useEffect(()=>{
        fetch(ENDPOINT+"/member")
        .then(response=>response.json())
        .then(data=>setName(data))
        .catch(error=>console.log("error"))
    },[])
    console.log(namee)
 return(
    
    <>
    <h1></h1>
    </>
 )
}

export default Home