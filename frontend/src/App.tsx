import { useState } from 'react'
import Logo from './assets/Eduardo_Bank_logo.jpg'
import './App.css'
import AquisitionChart, { type ChartResult } from "./AcquisitionsChart";

function App() {
  //this gives the component a memory//
  const [contribution, setContribution] = useState("");
  const [years, setyears] = useState("");
  const [result, setResult] = useState<CalculationResult | null>(null);
  const [error, setError] = useState("")
  type CalculationResult = {
    result: number;
    labels: string[];
    with_interest: number[];
    without_interest: number[];
    interest_only: number[];
    boost_only: number[];
  }
  

  async function calculate() {
    setResult(null);
    setError("");
    try{
  
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
      setResult(data);
    } else {
      setError(data.detail[0].msg);
    }
  } catch {
    setError("Could not reach the server. Is the API running?")
  }
  }

  return (
    <>
      <main>
        <header>
          <img src={Logo} className="logo" alt="Lifetime ISA Calculator logo" />
          <h1>Lifetime ISA Calculator</h1>
        </header>
    
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
          <button type="submit">Calculate</button>
        </form>
        <section aria-live="polite">

          {result !== null && (
            <div className="result">
              <span className="result-label">Estimated balance</span>
              <span className="result-amount">
              £
              {result.result.toLocaleString("en-GB", {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2,
              })}
              </span>
            </div>
          )}

        {error && <p className="error">{error}</p>}
        </section>
          <p>*Hover over the line to see data</p>
          <div className='chart'>
            {result && <AquisitionChart result={result}/>}
          </div>
        {result !== null && (
          <div className='table'>
            <table>
              <thead>
                <tr>
                  <th>Month</th>
                  <th>Contribution</th>
                  <th>Goverment Boost</th>
                  <th>Accrued Interest</th>
                  <th>Account end of the month</th>
                </tr>
              </thead>
              <tbody>
                {result.labels.map((label, i) => (
                  <tr key={label}>
                    <td>{label}</td>
                    <td>£{result.without_interest[i].toFixed(2)}</td>
                    <td>£{result.boost_only[i].toFixed(2)}</td>
                    <td>£{result.interest_only[i].toFixed(2)}</td>
                    <td>£{result.with_interest[i].toFixed(2)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
        </main>
    </>
  )
}
// .map: loops through every label and returns one table for each i//

export default App
