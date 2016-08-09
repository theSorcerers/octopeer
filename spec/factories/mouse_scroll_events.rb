FactoryGirl.define do
  factory :mouse_scroll_event do
    session
    sequence(:viewport_x)
    sequence(:viewport_y)
  end
end
