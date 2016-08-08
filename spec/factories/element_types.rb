FactoryGirl.define do
  factory :element_type do
    sequence(:name) { |n| "Element type #{n}" }
  end
end
