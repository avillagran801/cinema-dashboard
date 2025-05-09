import Header from "@/components/header";
import Loading from "@/components/loading";
import React from "react";

interface Movie {
  title: string;
  vote_average: number;
  vote_count: number;
  release_date: string;
  revenue: number;
  runtime: number;
  budget: number;
  original_language: string;
  original_title: string;
  overview: string;
  popularity: number;
  genres: string;
  production_companies: string;
  production_countries: string;
  spoken_languages: string;
  cast: string;
  director: string;
  imdb_rating: number;
  imdb_votes: number;
}


export default function Home() {
  const [loading, setLoading] = React.useState(true);
  const [data, setData] = React.useState<Movie[]>([]);

  React.useEffect(() => {
    fetch("http://localhost:8000/movies")
      .then(async res => {
        const json = await res.json();
        console.log("Fetched data:", json);
        setData(json);
      })
      .catch(err => console.error("Fetch error:", err));

    setLoading(false);
  }, []);

  if(loading){
    return(
      <Loading />
    )
  }

  return (
    <>
      <Header />
      <div style={{ padding: "2rem"}}>
        <div>
          {data && data.map((movie, index) => (
            <div key={index}>
              {movie.title}
            </div>
          ))}
        </div>
      </div>
    </>
  );
}
