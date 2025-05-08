import React from "react";

type DataPoint = {
  date: string;
  distributor: string;
  id: string;
  revenue: number;
  theaters: number;
  title: string;
}

export default function Home() {
  const [data, setData] = React.useState<DataPoint[]>([]);

  React.useEffect(() => {
    fetch("http://localhost:8000/data")
      .then(res => res.json())
      .then(setData);
  }, []);

  const test = data[0];
  console.log(test);

  return (
    <>
      <div style={{ 
        padding: "2rem",
        display: "flex",
        flexDirection: "column",
        gap: "1.4rem"
      }}>
        <h1>
          MI PRIMERA PÁGINA WEB
        </h1>
        <p>
          HOLA ESTA ES MI PAGNIA WEB LOS QUIERO MUCHO
        </p>
        <h2>
          NOELIA
        </h2>
        <p>
          ESTOY HACIENDO MI PAGINA WEB QUE EMOCION
        </p>
        <p>
          <b>
            BUENO Y AHORA QUE HAGO
          </b>
        </p>
        <p>
          <b>
            SI
          </b>
        </p>
        <p>
          © Todos los derechos reservados 2019
        </p>
      </div>
      <div style={{ padding: "2rem"}}>
        PRIMER DATO:
        <p>
          Fecha: {test.date}
        </p>
        <p>
          Distribuidor: {test.distributor}
        </p>
        <p>
          Id: {test.id}
        </p>
        <p>
          Ganancia: {test.revenue}
        </p>
        <p>
          Teatros: {test.theaters}
        </p>
        <p>
          Título: {test.title}
        </p>
      </div>
    </>
  );
}
