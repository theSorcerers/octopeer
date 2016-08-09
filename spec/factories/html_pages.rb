FactoryGirl.define do
  factory :html_page do
    session
    sequence(:dom) { |n| "<dom#{n}></dom#{n}>" }
  end
end
