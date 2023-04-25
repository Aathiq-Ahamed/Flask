import { useState,useEffect } from "react";
function Home(){
      const ENDPOINT = "http://127.0.0.1:5000";
      const [name,setName]=useState("")
      const [email,setEmail]=useState("")
      const [contact,setContact]=useState("")

 

   function clickme(event){
      setName("Aathiq Ahamed")
      setEmail("aathiqahamed333@gmail.com")
      setContact("0788080001")
      event.preventDefault();
      const data = {
      name,
      };

      fetch(ENDPOINT+"/member", {
      method: "POST",
      headers: {
      "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
      })
      .then(response=>response.json())
      .then(data=>setName(data))
      .catch(error=>console.log("error"))
}


   return(
      <div>
      <button onClick={clickme} >Click</button>

      <h1></h1>
      </div>
   )
}

export default Home