FactoryGirl.define do
  factory :keystroke_event do
    session
    keystroke_type
    sequence(:keystroke) { |n| "KEYSTROKE#{n}" }
  end
end
