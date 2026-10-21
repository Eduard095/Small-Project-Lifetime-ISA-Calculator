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

export type ChartResult = {
    labels: string[];
    with_interest_data: number[];
    without_interest_data: number[];
};

type Props = { result: ChartResult}


export default function AquisitionChart({ result }: Props) {
    const data = {
    labels: result.labels,          
    datasets: [
        {
            label: "contribution with interest",
            data: result.with_interest_data,
            borderColor: "#ee5519",
            backgroundColor: "#ee5519",
        },
         {
            label: "contribution without interest",
            data: result.without_interest_data,
            borderColor: "#2563eb",
            backgroundColor: "#2563eb",
        },
    ],
};
    return <Line data={data} />;
}