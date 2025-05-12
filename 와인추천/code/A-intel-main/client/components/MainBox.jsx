import React from "react"

const MainBox = ({ children }) => {
  return (
    <div className='flex justify-center px-24 py-14 items-center w-auto mx-auto h-auto rounded-xl shadow-2xl'>
      {children}
    </div>
  )
}

export default MainBox
