import React, { useEffect, useState } from "react"
import { useRouter } from "next/router"
import { fakeWineData } from "../../constants/fakeData"
import Result from "../../components/question/Result/Result"

const ResultPage = () => {
  const router = useRouter()
  const [wineData, setWineData] = useState([])
  useEffect(() => {
    //api요청  router.query.res
    setWineData(fakeWineData)
  })

  return (
    <div>
      {wineData.map((data, i) => (
        <Result data={data} key={i} />
      ))}
    </div>
  )
}

export default ResultPage
