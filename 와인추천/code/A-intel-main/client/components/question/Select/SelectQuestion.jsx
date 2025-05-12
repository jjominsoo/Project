import React from "react"
import Selection from "./Selection"

const SelectQuestion = ({
  list,
  userPreferences,
  currentQuestionIdx,
  updateUserPreferences,
}) => {
  return (
    <div className='ml-32'>
      {list.map((li, i) => (
        <Selection
          key={i}
          selectionContent={li}
          selectionNum={i}
          currentQuestionIdx={currentQuestionIdx}
          updateUserPreferences={updateUserPreferences}
          isSelected={userPreferences[currentQuestionIdx] === i}
        />
      ))}
    </div>
  )
}

export default SelectQuestion
