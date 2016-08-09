FactoryGirl.define do
  factory :window_resolution_event do
    session
    sequence(:width)
    sequence(:height)
  end
end
