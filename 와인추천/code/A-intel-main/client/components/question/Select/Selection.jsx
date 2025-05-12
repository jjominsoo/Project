import React from "react"

const Selection = ({
  selectionContent,
  selectionNum,
  currentQuestionIdx,
  updateUserPreferences,
  isSelected,
}) => {
  return (
    <button
      className={`block w-full text-left px-6 mt-4 py-2 text-4 border-b-2 border-main  transition duration-500 ease-in-out hover:bg-grey-300 transform hover:-translate-y-1 hover:scale-110
        ${isSelected && "bg-grey-300 "}
      `}
      onClick={() => updateUserPreferences(selectionNum, currentQuestionIdx)}
    >
      {selectionContent}
    </button>
  )
}

export default Selection
