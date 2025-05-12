import React from "react"
import { treeQuestions } from "../../../constants/questionList"
import Leaf from "./Leaf"

const TreeQuestion = ({
  leafs,
  currentQuestionIdx,
  userPreferences,
  updateUserPreferences,
  changeTreeQuestionNode,
}) => {
  return (
    <div className='mt-20 flex justify-center items-center'>
      {Object.keys(leafs).map((leaf, i) => (
        <Leaf
          content={leafs[leaf]}
          nodeN={leaf}
          updateUserPreferences={updateUserPreferences}
          preferN={i}
          currentQuestionIdx={currentQuestionIdx}
          isSelected={userPreferences[currentQuestionIdx] === i}
          changeTreeQuestionNode={changeTreeQuestionNode}
          key={i}
        />
      ))}
    </div>
  )
}

export default TreeQuestion
