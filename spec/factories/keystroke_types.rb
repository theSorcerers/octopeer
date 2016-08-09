FactoryGirl.define do
  factory :keystroke_type do
    sequence(:name) { |n| "Keystroke type #{n}" }
  end
end
