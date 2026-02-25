import { useState } from "react";

export default function App(){
  const [msg,setMsg]=useState("");
  const [chat,setChat]=useState([]);

  async function send(){
    const r=await fetch("http://localhost:8000/chat",{
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body:JSON.stringify({message:msg})
    });
    const j=await r.json();
    setChat([...chat,{r:"user",t:msg},{r:"ai",t:j.reply}]);
    setMsg("");
  }

  return (
    <div style={{background:"#111",color:"white",height:"100vh",padding:"20px"}}>
      <h2>Education GPT</h2>
      {chat.map((c,i)=><p key={i}><b>{c.r}:</b> {c.t}</p>)}
      <input value={msg} onChange={e=>setMsg(e.target.value)} />
      <button onClick={send}>Send</button>
    </div>
  );
}
