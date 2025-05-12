import React from "react"
import QuestionTitle from "../QuestionTitle"
import SelectQuestion from "./SelectQuestion"
import { selectQuestions } from "../../../constants/questionList"

const Select = ({
  currentQuestionIdx,
  updateUserPreferences,
  userPreferences,
}) => {
  return (
    <>
      <QuestionTitle title={selectQuestions[currentQuestionIdx].title} />
      <SelectQuestion
        list={selectQuestions[currentQuestionIdx].list}
        userPreferences={userPreferences}
        currentQuestionIdx={currentQuestionIdx}
        updateUserPreferences={updateUserPreferences}
      />
    </>
  )
}

export default Select
