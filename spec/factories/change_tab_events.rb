FactoryGirl.define do
  factory :change_tab_event do
    session
    sequence(:url) { |n| "http://url#{n}.com" }
  end
end
