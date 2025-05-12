import React from "react"
import Link from "next/link"

const ControlBar = ({
  userPreferences,
  currentQuestionIdx,
  controlQuestionIdx,
  length,
}) => {
  return (
    <div className='flex justify-end mt-10'>
      {currentQuestionIdx > 0 && (
        <button
          className='inline px-6 py-3 text-4 border-b-2 mr-4 border-main hover:bg-blue-200'
          onClick={() => controlQuestionIdx(false)}
        >
          Prev
        </button>
      )}
      {currentQuestionIdx === length - 2 ? (
        <Link
          href={{
            pathname: "/result",
            query: { res: JSON.stringify(userPreferences) },
          }}
        >
          <div className='inline px-6 py-3 text-4 border-b-2 border-main hover:bg-blue-100'>
            Submit
          </div>
        </Link>
      ) : (
        <button
          onClick={() => controlQuestionIdx(true)}
          className='inline px-6 py-3 text-4 border-b-2 border-main hover:bg-blue-100'
        >
          Next
        </button>
      )}
    </div>
  )
}

export default ControlBar
