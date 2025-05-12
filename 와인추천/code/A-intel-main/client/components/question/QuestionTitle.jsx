import React from "react"
import Logo from "../../images/Logo.png"

const QuestionTitle = ({ title, description }) => {
  return (
    <div className='flex align-center mt-10'>
      <img src={Logo.src} alt='logo' className='m-auto  w-16' />
      <div>
        <p className='ml-16 text-6 mt-2'>{title}</p>
        <p className='ml-16 text-4 mt-1'>{description || ""}</p>
      </div>
    </div>
  )
}

export default QuestionTitle
