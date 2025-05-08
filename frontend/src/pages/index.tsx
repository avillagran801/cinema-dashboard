import React from "react";

type Movie = {
  id: number;
  title: string;
  vote_average: number;
  vote_count: number;
  status: string;
  release_date: Date;
  revenue: number;
  runtime: number;
  budget: number;
  imdb_id: string;
}


export default function Home() {
  const [loading, setLoading] = React.useState(true);
  const [data, setData] = React.useState<Movie[]>([]);

  React.useEffect(() => {
    fetch("http://localhost:8000/data")
      .then(async res => {
        const json = await res.json();
        console.log("Fetched data:", json);
        setData(json);
        setLoading(false);
      })
      .catch(err => console.error("Fetch error:", err));
  }, []);

  if(loading){
    return(
      <>
        Cargando...
      </>
    )
  }

  return (
    <>
      <div style={{ padding: "2rem"}}>
        <div>
          <h1>
            PRIMERAS 200 PELÍCULAS DEL DATAFRAME 
          </h1>
        </div>
        <div>
          {data && data.map((movie) => (
            <div key={movie.id}>
              {movie.title}
            </div>
          ))}
        </div>
      </div>
    </>
  );
}
