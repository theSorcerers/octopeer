FactoryGirl.define do
  factory :event_type do
    sequence(:name) { |n| "Event type #{n}" }
  end
end
