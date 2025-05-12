import React, { useState } from "react"

const Evaluate = ({ index }) => {
  const [point, setPoint] = useState()
  const evaluatePoint = (e) => {
    const tmp = e.target.value.replace(/[^\d]/, "")
    const v = tmp > 10 ? 10 : tmp <= 0 ? 0 : tmp
    setPoint(v)
  }
  const submitResult = (index, point) => {
    console.log(index, +point)
  }
  return (
    <div className='flex justify-between w-full'>
      <div>
        <label>How was this wine?</label>
        <br />
        <input
          type='text'
          value={point || ""}
          onChange={(e) => evaluatePoint(e)}
          placeholder='0 ~ 10'
          className='placeholder-grey-500 text-main mt-3 text-6 outline-none w-18'
        />
      </div>
      <button
        className='inline px-4 text-4 border-b-2 border-main hover:bg-blue-200'
        onClick={() => submitResult(index, point)}
      >
        Complete
      </button>
    </div>
  )
}

export default Evaluate
