import { useState } from 'react'
import Logo from './assets/Eduardo_Bank_logo.png'
import './App.css'

function App() {
  //this gives the component a memory//
  const [count, setCount] = useState(0)
  const [contribution, setContribution] = useState("");
  const [years, setyears] = useState("");
  const [result, setResult] = useState<number | null>(null);

  async function calculate() {
    //send a request with fetch and await until API runs the calculator and comes back with an answer
    const response = await fetch("/calculation", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      //convert into JSON text to then convert to actual numbers
      body: JSON.stringify({
        contribution: Number(contribution),
        years: Number(years),
      }),
    });
    const data = await response.json();

    if(response.ok){
      setResult(data.result);
    }
    console.log("Status: ", response.status, "Data", data )
  }

  return (
    <>
      <section id="center">
        <div className="hero">
          <img src={Logo} className="logo" alt="Lifetime ISA Calculator logo" />
        </div>
        <div>
          <h1>Lifetime ISA Calculator</h1>
          <p>
            Edit <code>src/App.tsx</code> and save to test <code>HMR</code>
          </p>
        </div>
        <form
        onSubmit={(event) => {
          event.preventDefault();
          calculate()
        }}
        >
        <label>
          Monthly Contribution (£)
          <input
          type="number"
          value={contribution}
          //Whenever this box changes, take whatever now typed in it and save it as the contribution //
          onChange={(event => setContribution(event.target.value))}
          />
        </label>
        <label>
          Years until you buy
          <input
          type="number"
          value={years}
          onChange={(event => setyears(event.target.value))}
          />
        </label>
         <p>Contribution: {contribution}</p>
          <p>Years: {years}</p>

          <button type="submit">Calculate</button>

          {result !== null && (
            <p>
              Estimate balance: £
              {result.toLocaleString("en-GB", {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2,
              })}
            </p>
          )}
        </form>



        
        <button
          type="button"
          className="counter"
          onClick={() => setCount((count) => count + 1)}
        >
          Count is {count}
        </button>
      </section>
    </>
  )
}

export default App
