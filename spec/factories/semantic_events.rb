FactoryGirl.define do
  factory :semantic_event do
    session
    event_type
    element_type
  end
end
