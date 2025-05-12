import React from "react"
import Evaluate from "./Evaluate"

const countryFlag = {
  France: "France 🇫🇷",
  Italy: "Italy 🇮🇹",
  Spain: "Spain 🇪🇸",
  Australia: "Australia 🇦🇺",
  Argentina: "Argentina 🇦🇷",
  USA: "the United States 🇺🇸",
}

const Result = ({ data }) => {
  return (
    <div className='flex justify-center px-12 py-12 items-center mx-auto my-10 w-1/2 rounded-xl shadow-2xl text-main'>
      <div className='w-full'>
        <p className='text-6 mb-3'> {data.name}</p>
        <p className='text-4 mb-2'>{countryFlag[data.country] || "Etc 🇺🇳"}</p>
        <p className='text-4 mb-2'>{data.price}$</p>
        <Evaluate index={data.index} />
      </div>
    </div>
  )
}

export default Result
