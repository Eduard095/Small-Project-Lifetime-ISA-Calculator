import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    LineElement,
    PointElement,
    Tooltip,
    Legend,
} from "chart.js";

import {Line} from "react-chartjs-2"


ChartJS.register(CategoryScale,LinearScale,LineElement, PointElement, Tooltip, Legend)


const data = {
    labels: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    datasets: [
        {
            label: "Aquisition by month",
            data: [50,100,150, 200, 250, 300, 350, 400, 450, 500, 550, 600],
            borderColor: "#2563eb",
            backgroundColor: "#2563eb",
        },
    ],
};


export default function AquisitionChart() {
    return <Line data={data} />;
}